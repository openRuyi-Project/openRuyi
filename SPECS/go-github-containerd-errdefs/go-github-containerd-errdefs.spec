# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
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
#!RemoteAsset
Source0:        https://github.com/containerd/errdefs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/containerd/typeurl)

Provides:       go(github.com/containerd/errdefs) = %{version}

%description
A Go package for defining and checking common containerd errors.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
