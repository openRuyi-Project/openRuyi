# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/containerd/log

Name:           go-github-containerd-log
Version:        0.1.0
Release:        %autorelease
Summary:        Context-aware logging package for containerd
License:        Apache-2.0
URL:            https://github.com/containerd/log
#!RemoteAsset:  sha256:bfe14fa56ab57783e3ee827351e5704b04870cfb2a4aa03a13a7b2b81cc56c61
Source0:        https://github.com/containerd/log/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/log) = %{version}

Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/sys)

%description
Package log provides context-aware logging helpers used by containerd.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
