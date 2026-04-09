# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           mksh
Version:        59
Release:        %autorelease
Summary:        A fast, modern, and secure Korn Shell implementation
License:        MirOS and ISC and BSD-3-Clause
URL:            https://www.mirbsd.org/mksh.htm
VCS:            git:https://github.com/MirBSD/mksh
#!RemoteAsset
Source0:        https://github.com/MirBSD/mksh/archive/refs/tags/%{name}-R%{version}.tar.gz
Source1:        dot-mkshrc
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  ed

Requires(post):   grep
Requires(postun): sed

%description
mksh is the MirBSD Korn Shell, a modern, free implementation of the Korn
Shell language. It targets users who desire a compact, fast, reliable, and
secure shell with Unicode support.

# No configure
%conf

%build
export CFLAGS="%{optflags} -DMKSH_DISABLE_EXPERIMENTAL"
export LDFLAGS="%{build_ldflags}"

sh Build.sh -r
sh Build.sh -L -r

%install
# no makefile
install -D -m 755 mksh %{buildroot}%{_bindir}/mksh
install -D -m 755 lksh %{buildroot}%{_bindir}/lksh
install -D -m 644 mksh.1 %{buildroot}%{_mandir}/man1/mksh.1
install -D -m 644 lksh.1 %{buildroot}%{_mandir}/man1/lksh.1
install -D -m 644 dot.mkshrc %{buildroot}%{_sysconfdir}/mkshrc
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.mkshrc

%post
grep -q "^%{_bindir}/mksh$" %{_sysconfdir}/shells 2>/dev/null || \
  echo "%{_bindir}/mksh" >> %{_sysconfdir}/shells

%postun
if [ $1 -eq 0 ]; then
  sed -e 's@^%{_bindir}/mksh$@@' -e '/^$/d' -i %{_sysconfdir}/shells
fi

%files
%{_bindir}/mksh
%{_bindir}/lksh
%config(noreplace) %{_sysconfdir}/mkshrc
%config(noreplace) %{_sysconfdir}/skel/.mkshrc
%{_mandir}/man1/mksh.1*
%{_mandir}/man1/lksh.1*

%changelog
%autochangelog
