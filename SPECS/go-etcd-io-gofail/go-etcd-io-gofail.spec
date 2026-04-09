# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofail
%define go_import_path  go.etcd.io/gofail

Name:           go-etcd-io-gofail
Version:        0.2.0
Release:        %autorelease
Summary:        failpoints for go
License:        Apache-2.0
URL:            https://github.com/etcd-io/gofail
#!RemoteAsset
Source0:        https://github.com/etcd-io/gofail/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(go.etcd.io/gofail) = %{version}

%description
An implementation of failpoints for golang. Please read design.md for a deeper understanding.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
