# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           antithesis-sdk-go
%define go_import_path  github.com/antithesishq/antithesis-sdk-go
%define git_tag         v0.4.3-default-no-op

Name:           go-github-antithesishq-antithesis-sdk-go
Version:        0.4.3
Release:        %autorelease
Summary:        No-op Antithesis SDK for Go
License:        MIT
URL:            https://github.com/antithesishq/antithesis-sdk-go
#!RemoteAsset:  sha256:41c08320b4945a3b2864fe90e16ee2c7f483adb25e9be2bafdabbdd4f38a5457
Source0:        https://github.com/antithesishq/antithesis-sdk-go/archive/refs/tags/%{git_tag}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# GitHub tag v0.4.3-default-no-op unpacks as antithesis-sdk-go-0.4.3-default-no-op.
BuildOption(prep):  -n %{_name}-%{version}-default-no-op

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/antithesishq/antithesis-sdk-go) = %{version}

%description
No-op Antithesis SDK matching nats-server v2.11.1
(v0.4.3-default-no-op). Default nats-server builds use the local
internal/antithesis stubs; this module satisfies go.mod.

%prep -a
# tools/antithesis-go-instrumentor is a code generator that needs x/tools.
rm -rf tools

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
