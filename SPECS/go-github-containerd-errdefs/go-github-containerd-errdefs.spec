# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errdefs
%define go_import_path  github.com/containerd/errdefs

Name:           go-github-containerd-errdefs
Version:        1.0.0
Release:        %autorelease
Summary:        Common definition and library of errors used by containerd
License:        Apache-2.0
URL:            https://github.com/containerd/errdefs
#!RemoteAsset:  sha256:78573bda5a8376601590d570cd23e362ca2af3d3dc33d9ab3e6404852de33737
Source0:        https://github.com/containerd/errdefs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/typeurl)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/containerd/errdefs) = %{version}

%description
A Go package for defining and checking common containerd errors.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
