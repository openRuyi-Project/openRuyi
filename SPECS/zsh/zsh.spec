# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zsh
Version:        5.9
Release:        %autorelease
Summary:        Powerful interactive shell
License:        MIT-Modern-Variant AND ISC AND GPL-2.0-only
URL:            https://zsh.sourceforge.net/
VCS:            git:git://git.code.sf.net/p/zsh/code
#!RemoteAsset
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        zlogin.rhs
Source2:        zlogout.rhs
Source3:        zprofile.rhs
Source4:        zshrc.rhs
Source5:        zshenv.rhs
Source6:        dotzshrc
Source7:        dotzprofile
BuildSystem:    autotools

BuildOption(conf):  --with-term-lib="ncursesw"
BuildOption(conf):  --enable-cflags="%{optflags} -fPIE %(ncursesw6-config --cflags)"
BuildOption(conf):  --enable-ldflags="%(ncursesw6-config --libs) -pie -Wl,-z,relro"
BuildOption(conf):  --enable-cap
BuildOption(conf):  --enable-multibyte
BuildOption(conf):  --enable-pcre
BuildOption(conf):  --enable-zsh-secure-free
BuildOption(conf):  --enable-gdbm
BuildOption(conf):  --enable-maildir-support
BuildOption(conf):  --enable-etcdir=%{_sysconfdir}
BuildOption(conf):  --enable-fndir=%{_datadir}/%{name}/functions
BuildOption(conf):  --enable-site-fndir=%{_datadir}/%{name}/site-functions
BuildOption(conf):  --enable-scriptdir=%{_datadir}/%{name}/scripts
BuildOption(conf):  --enable-function-subdirs
BuildOption(conf):  --enable-multibyte
BuildOption(conf):  --with-tcsetpgrp
BuildOption(build):  all info html
BuildOption(install):  install.info
BuildOption(install):  fndir=%{_datadir}/%{name}/functions
BuildOption(install):  runhelpdir=%{_datadir}/%{name}/help

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  coreutils
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  texinfo

Provides:       /bin/zsh

%patchlist
# Upstream commit ab4d62eb975a4c4c51dd35822665050e2ddc6918
0001-zsh-Use-int-main-in-test-c-codes.patch
# upstream commit a84fdd7c8f77935ecce99ff2b0bdba738821ed79
0002-zsh-fix-module-loading-problem-with-full-RELRO.patch
# upstream commit 1b421e4978440234fb73117c8505dad1ccc68d46
0003-zsh-enable-PCRE-locale-switching.patch
# upstream commit b62e911341c8ec7446378b477c47da4256053dc0 and 10bdbd8b5b0b43445aff23dcd412f25cf6aa328a
0004-zsh-port-to-pcre2.patch
# upstream commit ecd3f9c9506c7720dc6c0833dc5d5eb00e4459c4
0005-zsh-support-texinfo-7.0.patch
# upstream commit 4c89849c98172c951a9def3690e8647dae76308f
0006-zsh-configure-c99.patch
# upstream commit d3edf318306e37d2d96c4e4ea442d10207722e94
0007-zsh-deletefilelist-segfault.patch
# avoid egrep warning break the tests
0008-zsh-5.9-do-not-use-egrep-in-tests.patch

%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

%package        html
Summary:        Zsh shell manual in html format
BuildArch:      noarch

%description    html
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in html format.

%conf -p
# Fix bindir path in some scripts
sed -i -e 's|%{_prefix}/local/bin|%{_bindir}|' \
    Misc/globtests.ksh Misc/globtests \
    Misc/lete2ctl Util/check_exports \
    Util/reporter Functions/VCS_Info/test-repo-git-rebase-*

autoreconf -fiv

%install -a
rm -rf %{buildroot}%{_bindir}/zsh-%{version}
rm -f  %{buildroot}%{_infodir}/dir

# Install system configuration files
mkdir -p %{buildroot}%{_sysconfdir}
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    install -m 644 $i %{buildroot}%{_sysconfdir}/"$(basename $i .rhs)"
done

# Install user configuration files
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/skel/.zshrc
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/skel/.zprofile

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
    echo "/bin/%{name}" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
    grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi

%files
%doc README LICENCE Etc/BUGS Etc/CONTRIBUTORS Etc/FAQ FEATURES MACHINES
%doc NEWS Etc/zsh-development-guide Etc/completion-style-guide
%attr(755,root,root) %{_bindir}/zsh
%{_mandir}/*/*
%{_infodir}/*
%{_datadir}/zsh
%{_libdir}/zsh
%config(noreplace) %{_sysconfdir}/skel/.z*
%config(noreplace) %{_sysconfdir}/z*

%files html
%doc Doc/*.html

%changelog
%autochangelog
