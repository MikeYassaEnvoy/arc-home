/**
 * Badge catalogue for the Home Edition season. Workstream E's art lives in
 * assets/badges/ keyed by id; ceremonies award leg badges via `onAwardBadge`.
 * The engine only awards the defaults below when nothing else does, so the
 * Badges screen is never empty.
 */
export interface BadgeDef {
  id: string;
  name: string;
  emoji: string;
  how: string;
}

export const BADGES: BadgeDef[] = [
  { id: 'race-rookie', name: 'Back in the Race', emoji: '🎒', how: 'Step on the starting mat for season two' },
  { id: 'kitchen-captain', name: 'Kitchen Captain', emoji: '🍳', how: 'Conquer the kitchen leg' },
  { id: 'brave-bite', name: 'Brave Bite', emoji: '🙈', how: 'Taste all three mystery bites blindfolded' },
  { id: 'backyard-explorer', name: 'Backyard Explorer', emoji: '🌿', how: 'Survive the Backyard Expedition' },
  { id: 'sock-ninja', name: 'Sock Ninja', emoji: '🧦', how: 'Match every sock in the pile' },
  { id: 'arcade-ace', name: 'Arcade Ace', emoji: '🕹️', how: 'Finish every heat of the Couch 500' },
  { id: 'race-champion', name: 'Race Champion', emoji: '🏆', how: 'Win the House Cup' },
  { id: 'first-win', name: 'First Win', emoji: '🥇', how: 'Finish a leg in first place' },
  { id: 'french-speaker', name: 'French Speaker', emoji: '🇫🇷', how: 'Order in French at Café Français' },
  { id: 'photographer', name: 'Photographer', emoji: '📸', how: 'Take 10 race photos' },
];

export const badgeById = (id: string): BadgeDef =>
  BADGES.find((b) => b.id === id) ?? { id, name: id, emoji: '🏅', how: '' };

/** Leg badges awarded by the engine if the ceremony does not award its own. */
export const DEFAULT_LEG_BADGE: Record<number, string[]> = {
  0: ['race-rookie'],
  1: ['kitchen-captain'],
  2: ['backyard-explorer'],
  3: ['sock-ninja'],
  4: ['arcade-ace'],
  5: ['race-champion'],
};
