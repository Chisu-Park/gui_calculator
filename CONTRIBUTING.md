## Contributing

First off, thank you for considering contributing to GUI-CALCULATOR. It's people
like you that make GUI-CALCULATOR such a great tool.

### Where do I go from here?

If you've noticed a bug or have a feature request, [make one][new issue]! It's
generally best if you get confirmation of your bug or approval for your feature
request this way before starting to code.

If you have a general question about activeadmin, you can post it on [Stack
Overflow], the issue tracker is only for bugs and feature requests.

### Fork & create a branch

If this is something you think you can fix, then [fork GUI-CALCULATOR] and create
a branch with a descriptive name.

### View your changes in a Rails application

GUI-CALCULATOR is meant to be used by humans, not cucumbers. So make sure to take
a look at your changes in a browser.

### Shipping a release (maintainers only)

Maintainers need to do the following to push out a release:

* Switch to the master branch and make sure it's up to date.
* Make sure you have [chandler] properly configured. Chandler is used to
  automatically submit github release notes from the changelog right after
  pushing the gem to rubygems.
* Run one of `bin/rake release:prepare_{prerelease,prepatch,patch,preminor,minor,premajor,major}`, push the result and create a PR.
* Review and merge the PR. The generated changelog in the PR should include all user visible changes you intend to ship.
* Run `bin/rake release` from the target branch once the PR is merged.

[chandler]: https://github.com/mattbrictson/chandler#2-configure-credentials
[Stack Overflow]: http://stackoverflow.com/questions/tagged/activeadmin
[new issue]: https://github.com/activeadmin/activeadmin/issues/new
[fork Active Admin]: https://help.github.com/articles/fork-a-repo
[make a pull request]: https://help.github.com/articles/creating-a-pull-request
[git rebasing]: http://git-scm.com/book/en/Git-Branching-Rebasing
[interactive rebase]: https://help.github.com/en/github/using-git/about-git-rebase
[shortcut reference links]: https://github.github.com/gfm/#shortcut-reference-link
[Rollup]: https://rollupjs.org/guide/en/#quick-start
[Yarn]: https://yarnpkg.com/en/docs/install
[Node.js]: https://nodejs.org/en/
