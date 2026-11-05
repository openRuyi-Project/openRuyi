# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 05a4d28642afce2e8efe43e312aada3f2abb70fa

Name:           cloop
Version:        0+git20261105.05a4d28
Release:        %autorelease
Summary:        Cross-language interface definition compiler
License:        LicenseRef-openRuyi-IDPL-1.0
URL:            https://github.com/asfernandes/cloop
VCS:            git:https://github.com/asfernandes/cloop.git
#!RemoteAsset:  sha256:3934d00a9dedd7110e2d174a736aaec6c67c1e52d0ade552d98f1288e4eb21d0
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
#!RemoteAsset:  sha256:94feb2e5f8a72fa9973808398385e291386163eb9f85df99be40fb85f2c35399
Source1:        https://raw.githubusercontent.com/FirebirdSQL/firebird/v5.0.4/builds/install/misc/IDPLicense.txt
BuildSystem:    cmake

BuildOption(prep):  -n %{name}-%{commit}

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++

%description
CLoop generates language bindings from an interface definition. Its
backends include C, C++ and Pascal.

%prep -a
cp -p %{SOURCE1} IDPLicense.txt

%install
install -Dpm 0755 %{_vpath_builddir}/bin/cloop %{buildroot}%{_bindir}/cloop

%files
%license IDPLicense.txt
%{_bindir}/cloop

%changelog
%autochangelog
