// Tag -> product map, shared by the EN and ES blog templates.
//
// Added 2026-10-07: the product pages were in the sitemap but had almost no inbound
// internal links (only the homepage and /products/ shipped any), so Google left them
// out of the index. Mapping each post's own tags to catalog entries gives every post
// real links into the catalog without hand-editing 109 files.
//
// Keys are lowercase on purpose: the tag vocabulary drifted over time, so both
// "Small Business" and "small business" exist in the frontmatter.
export const TAG_TO_PRODUCTS = {
  // receptionist / response channels
  'ai voice receptionist': ['voice-receptionist'],
  'voice receptionist': ['voice-receptionist'],
  'voice ai': ['voice-receptionist'],
  'ai text receptionist': ['text-receptionist'],
  'text receptionist': ['text-receptionist'],
  'whatsapp': ['text-receptionist'],
  'lead response': ['text-receptionist'],
  'lead follow-up': ['text-receptionist', 'ai-agent-setup'],
  'follow-up': ['text-receptionist'],
  'lead nurturing': ['text-receptionist', 'lead-generation-pack'],
  'lead conversion': ['text-receptionist', 'lead-generation-pack'],
  // lead generation
  'lead generation': ['lead-generation-pack'],
  'prospecting': ['lead-generation-pack'],
  'mls alerts': ['lead-generation-pack', 'ai-agent-setup'],
  'outreach': ['outreach-engine'],
  // agents and automation
  'ai agents': ['ai-agent-setup'],
  'ai agent': ['ai-agent-setup'],
  'ai': ['ai-agent-setup'],
  'automation': ['ai-agent-setup'],
  'business automation': ['ai-agent-setup'],
  'sales automation': ['ai-agent-setup'],
  'small business automation': ['ai-agent-setup'],
  'chatbots': ['ai-agent-setup'],
  'crm': ['business-ai-partner', 'ai-agent-setup'],
  'business intelligence': ['business-ai-partner'],
  'analytics': ['business-ai-partner'],
  'productivity': ['business-ai-partner'],
  'client onboarding': ['business-ai-partner'],
  'client experience': ['business-ai-partner'],
  // real estate
  'real estate': ['business-ai-partner', 'ai-agent-setup'],
  'real estate tech': ['ai-agent-setup', 'lead-generation-pack'],
  'real estate ai': ['ai-agent-setup'],
  'listing marketing': ['content-engine', 'ai-agent-setup'],
  'cma tools': ['ai-agent-setup'],
  'property management': ['care-maintenance'],
  'market data': ['ai-agent-setup'],
  // local visibility
  'seo': ['gbp-autopilot'],
  'local seo': ['gbp-autopilot'],
  'google business': ['gbp-autopilot'],
  'google tools': ['gbp-autopilot'],
  'customer reviews': ['review-engine'],
  // web and content
  'web design': ['free-audit', 'self-editing-cms'],
  'website audit': ['free-audit'],
  'wordpress': ['self-editing-cms'],
  'website builders': ['self-editing-cms'],
  'landing pages': ['content-engine'],
  'user experience': ['free-audit'],
  'mobile': ['free-audit'],
  'design': ['free-audit'],
  'digital marketing': ['content-engine'],
  'marketing': ['content-engine'],
  'content marketing': ['content-engine'],
  'content': ['content-engine'],
  'copywriting': ['content-engine'],
  'email marketing': ['content-engine'],
  'social media': ['content-engine'],
  'video marketing': ['content-engine'],
  'branding': ['content-booster', 'content-engine'],
  // commerce
  'e-commerce': ['self-editing-cms'],
  'selling online': ['self-editing-cms'],
  'online store': ['self-editing-cms'],
  'customer support': ['ai-agent-setup'],
  'case study': ['free-audit', 'ai-agent-setup'],
};

const norm = (t) => t.trim().toLowerCase();

/** Products matching a post's tags, max 3, deduped, with an entry-point fallback. */
export function getRelatedProducts(post, catalog, max = 3) {
  const slugs = [];
  for (const tag of post.data.tags) {
    slugs.push(...(TAG_TO_PRODUCTS[norm(tag)] ?? []));
  }
  // No tag matched the catalog: point at the two entry points rather than nothing.
  if (slugs.length < 2) slugs.push('free-audit', 'ai-agent-setup');
  return [...new Set(slugs)]
    .map((slug) => catalog.find((p) => p.slug === slug))
    .filter(Boolean)
    .slice(0, max);
}

/** Posts sharing at least one tag, most shared tags first, then newest. */
export function getRelatedPosts(post, allPosts, max = 3) {
  const own = new Set(post.data.tags.map(norm));
  return allPosts
    .filter((p) => p.id !== post.id)
    .map((p) => ({ post: p, shared: p.data.tags.filter((t) => own.has(norm(t))).length }))
    .filter((x) => x.shared > 0)
    .sort((a, b) => b.shared - a.shared || b.post.data.date.valueOf() - a.post.data.date.valueOf())
    .slice(0, max)
    .map((x) => x.post);
}
