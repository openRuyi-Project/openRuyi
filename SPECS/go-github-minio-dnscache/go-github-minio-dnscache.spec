# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dnscache
%define go_import_path  github.com/minio/dnscache
# Test failure due to network connection part
%define go_test_ignore_failure 1

Name:           go-github-minio-dnscache
Version:        0.1.1
Release:        %autorelease
Summary:        DNS lookup cache for Go
License:        MIT
URL:            https://github.com/minio/dnscache
#!RemoteAsset
Source0:        https://github.com/minio/dnscache/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sync)

Provides:       go(github.com/minio/dnscache) = %{version}

Requires:       go(golang.org/x/sync)

%description
DNS Lookup Cache

A fork from (https://github.com/rs/dnscache), however simplified to be
used with MinIO (https://github.com/minio/minio)

The dnscache package provides a DNS cache layer to Go's net.Resolver.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
