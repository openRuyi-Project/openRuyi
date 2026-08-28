# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gmsm
%define go_import_path  github.com/tjfoc/gmsm
# The gmcredentials test certificate has expired, and the websvr test expects
# a separately started local TLS server. The remaining packages are tested.
%define go_test_exclude %{go_import_path}/gmtls/gmcredentials %{go_import_path}/gmtls/websvr

Name:           go-github-tjfoc-gmsm
Version:        1.4.1
Release:        %autorelease
Summary:        Chinese cryptographic algorithms for Go
License:        Apache-2.0
URL:            https://github.com/tjfoc/gmsm
#!RemoteAsset:  sha256:fd6260fc92f5ca6d2e585c74121ecb2770f22da0eaa876da86215971dd2bcaea
Source0:        https://github.com/tjfoc/gmsm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/credentials)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/credentials)

%description
GMSM provides implementations of the SM2, SM3, and SM4 Chinese cryptographic
algorithms for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
