# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mock
%define go_import_path  go.uber.org/mock

Name:           go-uber-mock
Version:        0.4.0
Release:        %autorelease
Summary:        Mocking framework for Go
License:        Apache-2.0
URL:            https://github.com/uber/mock
VCS:            git:https://github.com/uber/mock.git
#!RemoteAsset:  sha256:30f28caf179b14a3a4f0ed28135904728e1bf61d78ba5fc4b89a36e301dd621b
Source0:        https://github.com/uber/mock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
# Nested test modules are included by the GOPATH-mode test discovery.
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(go.uber.org/mock) = %{version}
Provides:       go(go.uber.org/mock/gomock) = %{version}
Provides:       go(go.uber.org/mock/mockgen) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)

%description
Gomock is a mocking framework for Go. It integrates with Go's built-in testing
package and includes the mockgen source generator.

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
