# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tcsh
Version:        6.24.15
Release:        %autorelease
Summary:        C shell with file name completion and command line editing
License:        BSD-3-Clause
URL:            http://www.tcsh.org/
VCS:            git:https://github.com/tcsh-org/tcsh.git
#!RemoteAsset
Source0:        https://astron.com/pub/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-fix-nice-case-fail-if-noroot.patch

BuildOption(build):  all

BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  gcc

Provides:       /bin/csh
Provides:       /bin/tcsh
Provides:       csh = %{version}-%{release}

Requires(post): coreutils
Requires(post):  grep
Requires(postun): sed

%description
Tcsh is an enhanced but completely compatible version of the Berkeley
C-Shell, with the addition of a command line editor, command and file
name completion, listing, etc., and a bunch of small additions to the
shell itself.

%install -a
gzip $RPM_BUILD_ROOT%{_mandir}/man1/tcsh.1
rm -f          $RPM_BUILD_ROOT%{_bindir}/tcsh.old
ln -sf tcsh    $RPM_BUILD_ROOT%{_bindir}/csh
ln -sf tcsh.1.gz  $RPM_BUILD_ROOT%{_mandir}/man1/csh.1.gz

localedir="$RPM_BUILD_ROOT%{_datadir}/locale";
for lang in $(ls $localedir); do
    if [ -d $localedir/$lang ]; then
        dir="$localedir/$lang/LC_MESSAGES"
        if [[ -f "$dir/tcsh.cat" ]]; then
            mv $dir/tcsh.cat $dir/tcsh
            echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/tcsh"
        fi
    fi
done > %{name}.lang

%post
if [[ "$1" -eq 1 ]]; then
    if [[ ! -f %{_sysconfdir}/shells ]]; then
        echo "/bin/csh"        >> %{_sysconfdir}/shells
        echo "/bin/tcsh"       >> %{_sysconfdir}/shells
        echo "%{_bindir}/csh"  >> %{_sysconfdir}/shells
        echo "%{_bindir}/tcsh" >> %{_sysconfdir}/shells
    else
        grep -q "^/bin/csh$"        %{_sysconfdir}/shells || echo "/bin/csh"        >> %{_sysconfdir}/shells
        grep -q "^/bin/tcsh$"       %{_sysconfdir}/shells || echo "/bin/tcsh"       >> %{_sysconfdir}/shells
        grep -q "^%{_bindir}/csh$"  %{_sysconfdir}/shells || echo "%{_bindir}/csh"  >> %{_sysconfdir}/shells
        grep -q "^%{_bindir}/tcsh$" %{_sysconfdir}/shells || echo "%{_bindir}/tcsh" >> %{_sysconfdir}/shells
    fi
fi

%postun
if [[ "$1" -eq 0 && -f %{_sysconfdir}/shells ]]; then
    sed -i -e '\!^/bin/csh$!d'        %{_sysconfdir}/shells
    sed -i -e '\!^/bin/tcsh$!d'       %{_sysconfdir}/shells
    sed -i -e '\!^%{_bindir}/csh$!d'  %{_sysconfdir}/shells
    sed -i -e '\!^%{_bindir}/tcsh$!d' %{_sysconfdir}/shells
fi

%files -f %{name}.lang
%defattr(-,root,root)
%doc Copyright FAQ Fixes README.md complete.tcsh
%{_bindir}/tcsh
%{_bindir}/csh
%{_mandir}/man1/*.1*

%changelog
%autochangelog
