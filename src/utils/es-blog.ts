import { getCollection, type CollectionEntry } from 'astro:content';

export type PreferredPost = { entry: CollectionEntry<'blog'>; slug: string };

const baseSlug = (id: string) => id.replace(/-es$/, '');

/**
 * The Spanish blog pairs each English post with an optional Spanish translation.
 *
 * Translations live in the same collection as `<slug>-es.md` and are served at the
 * same URL as before, `/es/blog/<slug>/`, so no indexed URL has to change and the
 * hreflang pair stays intact. Until a translation exists, the Spanish URL falls back
 * to the English post rather than disappearing, which is what makes it safe to
 * translate this blog in batches.
 */
export async function getEsBlogPosts(): Promise<PreferredPost[]> {
  const all = await getCollection('blog');
  const esBySlug = new Map(
    all.filter((p) => p.data.lang === 'es').map((p) => [baseSlug(p.id), p] as const),
  );

  const preferred: PreferredPost[] = all
    .filter((p) => p.data.lang === 'en')
    .map((p) => ({ entry: esBySlug.get(p.id) ?? p, slug: p.id }));

  // A Spanish post with no English twin still needs to be reachable.
  for (const [slug, entry] of esBySlug) {
    if (!all.some((p) => p.data.lang === 'en' && p.id === slug)) preferred.push({ entry, slug });
  }

  return preferred.sort((a, b) => b.entry.data.date.valueOf() - a.entry.data.date.valueOf());
}

/** Slugs of English posts that already have a Spanish translation. */
export async function getTranslatedBlogSlugs(): Promise<Set<string>> {
  const all = await getCollection('blog');
  return new Set(all.filter((p) => p.data.lang === 'es').map((p) => baseSlug(p.id)));
}
