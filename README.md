# So what's this?

## Background:

A common theme with all social media that I've tried is that separating signal from noise is difficult (I'd even count IRC as a social media ...)
However, each service / technology seems to have their unique problems regarding the SNR.

I like the *idea* of [Mastodon](https://github.com/tootsuite/mastodon) (federated, open source, open protocol Twitter-like service) very much.
But as Mastodon 'toots' are scattered across a large number of instances and themes of instance vary *a lot* ... in practice, Mastodon is a slightly uneven experience.
With Mastodon, the problem is *finding* the activity across the fediverse (Twitter OTOH has a problem of overabundance of activity.)

* The local timeline on mathstodon.xyz instance is relatively quiet; there's only a handful of active people. While this isn't *bad* (on the contrary, it's refreshing to see a timeline one *can* read in full even if you check it once a week), it isn't particularly engaging either.
* The local federated timeline om mathstodon.xyz is just weird. Because most people and the people they follow have *very* varying interests, it contains stuff that I can best describe as "random assortment of things and stuff", not following any particular "math" theme.
* A large number of English-language Mastodon instances seem to contain lots of "generic social chatter" or politics. While I have nothing in particular against them, neither is something on which I particularly wish to spend any more of my time than I currently do. So switching from the quiet-but-mathy Mathstodon to some other instance isn't a solution.
* (And then there's popular instances that have French and Japanese as main languages ... Unfortunately, I speak neither. Maybe I should learn? :P)
* Tl;dr. It's a hassle to populate my local timeline with interesting things.

## An attempted solution:

So what I did: I [previewed](http://www.unmung.com/mastoview?url=mathstodon.xyz&view=local) *many* instances with a 3rd party tool (thanks to open protocols!), trying to find people 1) who toot regularly 2) on subjects that at least align with my interests (maths, science fiction, sciences, etc)  and 3) toot in English. And then proceeded to "remote follow" them. Unfortunately it appears remote follows don't work perfectly as you might expect (in particular, I noticed that *not* everything someone tooted on e.g bookwitty.social gets pulled to mathstodon.xyz), but I'm not thrilled about an idea to create n+1 accounts on various instances either.

And anyway, then I dumped my follows list into csv here.

The list is not very well curated (it's simply a dump of my mathstodon follows; it contains both active and inactive people). It exists in two forms: csv that can be imported to mastodon (`following_accounts.csv`) and a txt file of links `tooterslist.txt`.

* Note. Follow != endorsement.

Instances currently included in the listing:
* mathstodon.xyz
* mastodon.zaclys.com
* scifi.fyi
* bookwitty.social
* mastodon.social
* octodon.social

Other possibly interesting instances:
* mastodon.technology
* cybre.space
* scholar.social
* moseisley.club
* im-in.space

Inspected their local timelines with https://m6n-view.hnle.tk/ and http://www.unmung.com/mastoview?url=mathstodon.xyz&view=local
Found them via https://instances.social

