# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global build_number 1812-0

Name:           firebird-btyacc
Version:        5.0.4
Release:        %autorelease
Summary:        Backtracking SQL parser generator for Firebird
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/FirebirdSQL/firebird
VCS:            git:https://github.com/FirebirdSQL/firebird.git
#!RemoteAsset:  sha256:5041b97b480c9fe241c92ad0adf89e36faad0a8f0e21f1371dfbcc96a6f38e12
Source0:        %{url}/releases/download/v%{version}/Firebird-%{version}.%{build_number}-source.tar.xz

BuildRequires:  make

%description
Firebird's BtYacc generates separate SQL keyword and semantic type guards
and accepts the grammar extensions used by the Firebird SQL parser.

%prep
%autosetup -p1 -n Firebird-%{version}.%{build_number}-source
sed -e 's/\<YACC\>/FIREBIRD-BTYACC/g' -e 's/\<[Yy]acc\>/firebird-btyacc/g' \
    extern/btyacc/manpage > firebird-btyacc.1

%build
%make_build -C extern/btyacc CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
install -Dpm 0755 extern/btyacc/btyacc %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 firebird-btyacc.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license extern/btyacc/README extern/btyacc/README.BYACC
%{_bindir}/firebird-btyacc
%{_mandir}/man1/firebird-btyacc.1*

%changelog
%autochangelog
