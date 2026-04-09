# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pbzip2
Version:        1.1.13
Release:        %autorelease
Summary:        Parallel implementation of bzip2
License:        MIT
URL:            https://launchpad.net/pbzip2
VCS:            git:https://github.com/ruanhuabin/pbzip2
#!RemoteAsset
Source0:        https://launchpad.net/pbzip2/1.1/%{version}/+download/pbzip2-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.

%prep -a
iconv -f iso-8859-1 -t utf-8 AUTHORS > AUTHORS.utf8 && mv AUTHORS.utf8 AUTHORS

# No configure.
%conf

%install -a
install -D -m755 pbzip2 %{buildroot}%{_bindir}/pbzip2
install -D -m644 pbzip2.1 %{buildroot}%{_mandir}/man1/pbzip2.1
ln -sf pbzip2 %{buildroot}%{_bindir}/pbunzip2
ln -sf pbzip2 %{buildroot}%{_bindir}/pbzcat

# No tests.
%check

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/pbzip2
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_mandir}/man1/pbzip2.1*

%changelog
%autochangelog
