# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lazycore
%define go_import_path  github.com/jesseduffield/lazycore
%define commit_id       03d2e40243c5df6b011bca3e91f80b900e7eeda7

Name:           go-github-jesseduffield-lazycore
Version:        0+git20260621.03d2e40
Release:        %autorelease
Summary:        Shared functionality for lazygit, lazydocker, etc
License:        MIT
URL:            https://github.com/jesseduffield/lazycore
#!RemoteAsset:  sha256:c2d63a66d82d581ce5d111abf53ae0a92a6fffeb362e4d66b55085fd4113732c
Source0:        https://github.com/jesseduffield/lazycore/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/jesseduffield/lazycore) = %{version}

Requires:       go(github.com/samber/lo)
Requires:       go(github.com/stretchr/testify)

%description
lazycore provides shared core utilities used by the lazygit and lazydocker projects.

%check
# Compile every package and its tests before tolerating the environment check.
%buildsystem_golangmodules_check -run '^$'
# TestGetLazyRootDirectory expects the checkout to be inside a lazygit or
# lazydocker source tree, which is not true in the isolated RPM build directory.
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
