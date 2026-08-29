# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           genproto-googleapis-cloud-extendedops
%define go_import_path  google.golang.org/genproto/googleapis/cloud/extendedops
%define commit_id       aa98bba5eb94e5dcff65e3ffaf9d216c8252207d

Name:           go-google-genproto-googleapis-cloud-extendedops
Version:        0+git20260607.aa98bba5
Release:        %autorelease
Summary:        Generated extended operations protos for Google Cloud clients
License:        Apache-2.0
URL:            https://github.com/googleapis/go-genproto
#!RemoteAsset:  sha256:81d6931f5f240d25c1e13b62e7c63a5fdd368593280d6f587abd169b4b1d9788
Source0:        https://github.com/googleapis/go-genproto/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# This generated leaf package has no independent go.mod. Package only this
# source subtree so the root go-genproto package does not need to be upgraded
# just to satisfy cloud.google.com/go/compute. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(google.golang.org/genproto/googleapis/cloud/extendedops) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
This package provides generated extended operation protobuf types for Google
Cloud Go clients.

%install
install -dm0755 %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a googleapis/cloud/extendedops/*.go %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%check
mkdir -p _build/src/google.golang.org/genproto/googleapis/cloud
cp -a googleapis/cloud/extendedops _build/src/%{go_import_path}
GO111MODULE=off GOPATH="$PWD/_build:%{_datadir}/gocode" go test -v %{go_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
