# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

# We can't build these right now
# Change these to 1 once we can
%bcond docs 0
%bcond cvs 0
%bcond libsecret 0

Name:           git
Version:        2.51.0
Release:        %autorelease
Summary:        Fast Version Control System
License:        BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://git-scm.com/
VCS:            git:https://github.com/git/git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/software/scm/git/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.kernel.org/pub/software/scm/git/%{name}-%{version}.tar.sign
Source2:        gitweb-httpd.conf
Source3:        gitweb.conf.in
Source4:        git@.service.in
Source5:        git.socket
BuildSystem:    autotools

# CVE-2024-52005: https://github.com/gitgitgadget/git/pull/1853
Patch0:         0001-git-2.51-sanitize-sideband-channel-messages.patch

BuildOption(build):  all

BuildRequires:  acl
BuildRequires:  bash
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  xz
BuildRequires:  systemd-rpm-macros
BuildRequires:  perl(Error)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Mail::Address)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(bash-completion)
%if %{with docs}
BuildRequires:  docbook-style-dsssl
BuildRequires:  rubygem-asciidoctor
BuildRequires:  perl(File::Compare)
BuildRequires:  xmlto
BuildRequires:  linkchecker
%endif
%if %{with cvs}
BuildRequires:  cvs
BuildRequires:  cvsps
%endif

Requires:       git-core = %{version}-%{release}
Requires:       git-core-doc = %{version}-%{release}
Requires:       perl-Git = %{version}-%{release}

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs common set of tools which are usually using with
small amount of dependencies. To install all git packages, including
tools for integrating with other SCMs, install the git-all meta-package.

%package        core
Summary:        Core package of git with minimal functionality
Requires:       less
Requires:       openssh-clients
Requires:       zlib

%description    core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git-core rpm installs really the core tools with minimal
dependencies. Install git package for common set of tools.
To install all git packages, including tools for integrating with
other SCMs, install the git-all meta-package.

%package        core-doc
Summary:        Documentation files for git-core
BuildArch:      noarch
Requires:       git-core = %{version}-%{release}

%description    core-doc
Documentation files for git-core package including man pages.

%if %{with libsecret}
%package        credential-libsecret
Summary:        Git helper for accessing credentials via libsecret
BuildRequires:  libsecret-devel
Requires:       git = %{version}-%{release}

%description    credential-libsecret
Git helper for accessing credentials via libsecret.
%endif

%if %{with cvs}
%package        cvs
Summary:        Git tools for importing CVS repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       cvs
Requires:       cvsps
Requires:       perl(DBD::SQLite)

%description    cvs
Git tools for importing CVS repositories.
%endif

%package        daemon
Summary:        Git protocol daemon
Requires:       git-core = %{version}-%{release}
%{?systemd_requires}

%description    daemon
The git daemon for supporting git:// access to git repositories.

%package        email
Summary:        Git tools for sending patches via email
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       perl(Authen::SASL)
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(File::Spec::Functions)
Requires:       perl(File::Temp)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Mail::Address)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::QuotedPrint)
Requires:       perl(Net::Domain)
Requires:       perl(Net::SMTP)
Requires:       perl(Net::SMTP::SSL)
Requires:       perl(POSIX)
Requires:       perl(Sys::Hostname)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)
Requires:       perl(Text::ParseWords)

%description    email
Git tools for sending patches via email.

%package     -n gitk
Summary:        Git repository browser
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       git-gui = %{version}-%{release}
Requires:       tk

%description -n gitk
Git repository browser.

%package     -n gitweb
Summary:        Simple web interface to git repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}

%description -n gitweb
Simple web interface to git repositories.

%package        gui
Summary:        Graphical interface to Git
BuildArch:      noarch
Requires:       gitk = %{version}-%{release}
Requires:       tk

%description    gui
Graphical interface to Git.

%package        p4
Summary:        Git tools for working with Perforce depots
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
Requires:       git = %{version}-%{release}

%description    p4
Git tools for working with Perforce depots.

%package     -n perl-Git
Summary:        Perl interface to Git
BuildArch:      noarch
Requires:       git = %{version}-%{release}

%description -n perl-Git
Perl interface to Git.

%package     -n perl-Git-SVN
Summary:        Perl interface to Git::SVN
BuildArch:      noarch
Requires:       git = %{version}-%{release}

%description -n perl-Git-SVN
Perl interface to Git::SVN.

%package        subtree
Summary:        Git tools to merge and split repositories
BuildArch:      noarch
Requires:       git-core = %{version}-%{release}

%description    subtree
Git subtrees allow subprojects to be included within a subdirectory
of the main project, optionally including the subproject's entire
history.

%package        svn
Summary:        Git tools for interacting with Subversion repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       perl(Digest::MD5)
Requires:       perl(Term::ReadKey)
Requires:       subversion

%description    svn
Git tools for interacting with Subversion repositories.

%prep -a
%if %{without cvs}
# Remove git-cvs* from command list
sed -i '/^git-cvs/d' command-list.txt
%endif

# Use these same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
cat << \EOF | tee config.mak
CFLAGS = %{optflags}
GITWEB_CONFIG = "%{_sysconfdir}/gitweb.conf"
GITWEB_PROJECTROOT = "%{_localstatedir}/lib/git"
%if %{with docs}
USE_ASCIIDOCTOR = YesPlease
%endif
PYTHON_PATH = %{_bindir}/python3
USE_LIBPCRE2 = YesPlease
NO_PERL_CPAN_FALLBACKS = 1
prefix = %{_prefix}
mandir = %{_mandir}
htmldir = %{_docdir}/git
perllibdir = %{perl_vendorlib}
gitexecdir = %{_libexecdir}/git
gitwebdir = %{_localstatedir}/www/git
V = 1
EOF

# Move contrib/{contacts,subtree} docs to Documentation so they build with the
# proper asciidoc/docbook/xmlto options
mv contrib/{contacts,subtree}/git-*.adoc Documentation/

%conf
# No conf

%build -p
# Improve build reproducibility
export TZ=UTC
export SOURCE_DATE_EPOCH=$(date -r version +%%s 2>/dev/null)

%build -a
%make_build -C contrib/contacts/ all
%if %{with libsecret}
%make_build -C contrib/credential/libsecret/
%endif
%make_build -C contrib/credential/netrc/
%make_build -C contrib/diff-highlight/
%make_build -C contrib/subtree/ all

# Remove contrib/fast-import/import-zips.py which requires python2.
rm -rf contrib/fast-import/import-zips.py

%install -a
%make_install -C contrib/contacts
%if %{with libsecret}
install -pm 755 contrib/credential/libsecret/git-credential-libsecret \
    %{buildroot}%{_libexecdir}/git
%endif

install -pm 755 contrib/credential/netrc/git-credential-netrc \
    %{buildroot}%{_libexecdir}/git

%make_install -C contrib/subtree

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{gitweb_httpd_conf}
sed "s|@PROJECTROOT@|%{_localstatedir}/lib/git|g" \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/gitweb.conf

# install contrib/diff-highlight
install -Dpm 0755 contrib/diff-highlight/diff-highlight \
   %{buildroot}%{_datadir}/git/contrib/diff-highlight

%if %{without cvs}
# Remove git-cvs* and gitcvs*
find %{buildroot} Documentation \( -type f -o -type l \) \
    \( -name 'git-cvs*' -o -name 'gitcvs*' \) -exec rm -f {} ';'
%endif

mkdir -p %{buildroot}%{_localstatedir}/lib/git
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/git.socket
perl -p \
    -e "s|\@GITEXECDIR\@|%{_libexecdir}/git|g;" \
    -e "s|\@BASE_PATH\@|%{_localstatedir}/lib/git|g;" \
    %{SOURCE4} > %{buildroot}%{_unitdir}/git@.service

# Remove unneeded git-remote-testsvn so git-svn can be noarch
rm -f %{buildroot}%{_libexecdir}/git/git-remote-testsvn

# Generate %%files list for convinience of packagers
exclude_re="email|git-(citool|credential-libsecret|cvs|daemon|gui|instaweb|p4|subtree|svn)|gitk|gitweb|p4merge"
(find %{buildroot}{%{_bindir},%{_libexecdir}} -type f -o -type l | grep -vE "$exclude_re" | sed -e s@^%{buildroot}@@) > bin-man-doc-files
(find %{buildroot}{%{_bindir},%{_libexecdir}} -mindepth 1 -type d | grep -vE "$exclude_re" | sed -e 's@^%{buildroot}@%dir @') >> bin-man-doc-files
(find %{buildroot}%{perl_vendorlib} -type f | sed -e s@^%{buildroot}@@) > perl-git-files
(find %{buildroot}%{perl_vendorlib} -mindepth 1 -type d | sed -e 's@^%{buildroot}@%dir @') >> perl-git-files
# Split out Git::SVN files
grep Git/SVN perl-git-files > perl-git-svn-files
sed -i "/Git\/SVN/ d" perl-git-files
%if %{with docs}
(find %{buildroot}%{_mandir} -type f | grep -vE "$exclude_re|Git" | sed -e s@^%{buildroot}@@ -e 's/$/*/' ) >> bin-man-doc-files
%else
rm -rf %{buildroot}%{_mandir}
%endif

# Setup bash completion
install -Dpm 644 contrib/completion/git-completion.bash %{buildroot}%{bash_completions_dir}/git
ln -s git %{buildroot}%{bash_completions_dir}/gitk

# Install tcsh completion
mkdir -p %{buildroot}%{_datadir}/git/contrib/completion
install -pm 644 contrib/completion/git-completion.tcsh \
    %{buildroot}%{_datadir}/git/contrib/completion/

# Install git-prompt.sh
mkdir -p %{buildroot}%{_datadir}/git/contrib/completion
install -pm 644 contrib/completion/git-prompt.sh \
    %{buildroot}%{_datadir}/git/contrib/completion/

# find translations
%find_lang %{name} %{name}.lang
cat %{name}.lang >> bin-man-doc-files

# Delete unwanted files
find . -regex '.*/\.\(git\(attributes\|ignore\)\|perlcriticrc\)' -delete
chmod a-x Documentation/technical/api-index.sh
find contrib -type f -print0 | xargs -r0 chmod -x

# Split core files
not_core_re="git-(add--interactive|contacts|credential-netrc|filter-branch|instaweb|request-pull|send-mail)|gitweb"
grep -vE "$not_core_re|%{_mandir}" bin-man-doc-files > bin-files-core
touch man-doc-files-core
%if %{with docs}
grep -vE "$not_core_re" bin-man-doc-files | grep "%{_mandir}" > man-doc-files-core
%endif
grep -E  "$not_core_re" bin-man-doc-files > bin-man-doc-git-files

# Install docs
mkdir -p "%{buildroot}/%{_docdir}/git" "%{buildroot}/%{_docdir}/git/howto" "%{buildroot}/%{_docdir}/git/technical"
cp -a README.md Documentation/*.adoc "%{buildroot}/%{_docdir}/git/"
cp -a Documentation/howto/*.adoc "%{buildroot}/%{_docdir}/git/howto/"
cp -a Documentation/technical/*.adoc "%{buildroot}/%{_docdir}/git/technical/"
%if %{with docs}
cp -a Documentation/*.html "%{buildroot}/%{_docdir}/git/"
cp -a Documentation/howto/*.html "%{buildroot}/%{_docdir}/git/howto/"
cp -a Documentation/technical/*.html "%{buildroot}/%{_docdir}/git/technical/"
%endif

cp -p gitweb/INSTALL %{buildroot}%{_docdir}/git/INSTALL.gitweb
cp -p gitweb/README %{buildroot}%{_docdir}/git/README.gitweb
cp -pr CODE_OF_CONDUCT.md README.md Documentation/*.adoc Documentation/RelNotes contrib %{buildroot}%{_docdir}/git/
# place doc files into %{_docdir}/git and split them into expected packages
not_core_doc_re="(git-(cvs|gui|citool|daemon|instaweb|subtree))|p4|svn|email|gitk|gitweb"
{
    find %{buildroot}%{_docdir}/git -type f -maxdepth 1 \
        | grep -o "%{_docdir}/git.*$" \
        | grep -vE "$not_core_doc_re"
    find %{buildroot}%{_docdir}/git/{contrib,RelNotes,howto,technical} -type f \
        | grep -o "%{_docdir}/git.*$"
    find %{buildroot}%{_docdir}/git -type d | grep -o "%{_docdir}/git.*$" \
        | sed "s/^/\%dir /"
} >> man-doc-files-core

%post daemon
%systemd_post git.socket

%preun daemon
%systemd_preun git.socket

%postun daemon
%systemd_postun_with_restart git.socket

%files -f bin-man-doc-git-files
%{_datadir}/git/contrib/diff-highlight

%files core -f bin-files-core
%license COPYING
# exclude is best way here because of troubles with symlinks inside git/
%exclude %{_datadir}/git/contrib/diff-highlight
%{bash_completions_dir}/git
%{_datadir}/git/
%{_datadir}/git-core/

%files core-doc -f man-doc-files-core

%if %{with libsecret}
%files credential-libsecret
%{_libexecdir}/git/git-credential-libsecret
%endif

%if %{with cvs}
%files cvs
%{_docdir}/git/*git-cvs*.adoc
%{_bindir}/git-cvsserver
%{_libexecdir}/git/*cvs*
%if %{with docs}
%{_mandir}/man1/*cvs*.1*
%{_docdir}/git/*git-cvs*.html
%endif
%endif

%files daemon
%{_docdir}/git/git-daemon*.adoc
%{_unitdir}/git.socket
%config(noreplace) %{_unitdir}/git@.service
%{_libexecdir}/git/git-daemon
%{_localstatedir}/lib/git
%if %{with docs}
%{_mandir}/man1/git-daemon*.1*
%{_docdir}/git/git-daemon*.html
%endif

%files email
%{_docdir}/git/*email*.adoc
%{_libexecdir}/git/*email*
%if %{with docs}
%{_mandir}/man1/*email*.1*
%{_docdir}/git/*email*.html
%endif

%files -n gitk
%{_docdir}/git/*gitk*.adoc
%{_bindir}/*gitk*
%{_datadir}/gitk
%{bash_completions_dir}/gitk
%if %{with docs}
%{_mandir}/man1/*gitk*.1*
%{_docdir}/git/*gitk*.html
%endif

%files -n gitweb
%{_docdir}/git/*.gitweb
%{_docdir}/git/gitweb*.adoc
%{_libexecdir}/git/git-instaweb
%{_docdir}/git/git-instaweb.adoc
%if %{with docs}
%{_mandir}/man1/gitweb.1*
%{_mandir}/man5/gitweb.conf.5*
%{_docdir}/git/gitweb*.html
%{_mandir}/man1/git-instaweb.1*
%{_docdir}/git/git-instaweb.html
%endif
%config(noreplace)%{_sysconfdir}/gitweb.conf
%config(noreplace)%{_sysconfdir}/httpd/conf.d/%{gitweb_httpd_conf}
%{_localstatedir}/www/git/

%files gui
%{_libexecdir}/git/git-gui*
%{_libexecdir}/git/git-citool
%{_datadir}/git-gui/
%{_docdir}/git/git-gui.adoc
%{_docdir}/git/git-citool.adoc
%if %{with docs}
%{_mandir}/man1/git-gui.1*
%{_docdir}/git/git-gui.html
%{_mandir}/man1/git-citool.1*
%{_docdir}/git/git-citool.html
%endif

%files p4
%{_libexecdir}/git/*p4*
%{_libexecdir}/git/mergetools/p4merge
%{_docdir}/git/*p4*.adoc
%if %{with docs}
%{_mandir}/man1/*p4*.1*
%{_docdir}/git/*p4*.html
%endif

%files -n perl-Git -f perl-git-files
%if %{with docs}
%{_mandir}/man3/Git.3pm*
%endif

%files -n perl-Git-SVN -f perl-git-svn-files

%files subtree
%{_libexecdir}/git/git-subtree
%{_docdir}/git/git-subtree.adoc
%if %{with docs}
%{_mandir}/man1/git-subtree.1*
%{_docdir}/git/git-subtree.html
%endif

%files svn
%{_libexecdir}/git/git-svn
%{_docdir}/git/git-svn.adoc
%if %{with docs}
%{_mandir}/man1/git-svn.1*
%{_docdir}/git/git-svn.html
%endif

%changelog
%autochangelog
