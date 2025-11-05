# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       294c46522620afffd7b57af7ef743131ff55a488
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           trinity
Version:        1.9+git20260225.%{shortcommit}
Release:        %autorelease
Summary:        A Linux System call fuzz tester
License:        GPL-2.0-only
URL:            https://github.com/kernelslacker/trinity
#!RemoteAsset
Source0:        https://github.com/kernelslacker/trinity/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -p1 -n %{name}-%{commit}
BuildOption(build):  DEVEL=0
BuildOption(install):  DESTDIR=%{buildroot}%{_prefix}

%description
Trinity makes syscalls at random, with random arguments. Where Trinity
differs from other fuzz testers is that the arguments it passes are not
purely random.

%conf -p
export CFLAGS="%{optflags}"

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 trinity.1 \
  %{buildroot}%{_mandir}/man1/trinity.1

# Install helper scripts
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -p scripts/* %{buildroot}%{_libexecdir}/%{name}
chmod a+x %{buildroot}%{_libexecdir}/%{name}/privs.sh

# No tests.
%check

%files
%license COPYING
%doc README
%{_bindir}/trinity
%{_libexecdir}/%{name}/
%{_mandir}/man1/trinity.1*

%changelog
%{?autochangelog}
