# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zsh
Version:        5.9.1
Release:        %autorelease
Summary:        Powerful interactive shell
License:        MIT-Modern-Variant AND ISC AND GPL-2.0-only
URL:            https://zsh.sourceforge.net/
VCS:            git:git://git.code.sf.net/p/zsh/code
#!RemoteAsset:  sha256:5d20bec03f981dc4e9a09ec245e7415388ff641f79c5c5c416b5042e58d8280d
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
BuildRequires:  groff

Provides:       /bin/zsh

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
