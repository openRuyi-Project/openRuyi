# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           esbuild
%define go_import_path  github.com/evanw/esbuild

Name:           go-github-evanw-esbuild
Version:        0.28.2
Release:        %autorelease
Summary:        JavaScript and CSS bundler and minifier written in Go
License:        MIT
URL:            https://github.com/evanw/esbuild
#!RemoteAsset:  sha256:300162f899361d9f0263065f8728ef9086dcfc1a3d36bcbc4e0abe5de9c58bf8
Source0:        https://github.com/evanw/esbuild/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/pkg/api) = %{version}
Provides:       go(%{go_import_path}/pkg/cli) = %{version}

Requires:       go(golang.org/x/sys)

%description
Esbuild is a JavaScript and CSS bundler and minifier implemented in Go. This
package installs the complete Go module, including its public API and CLI
packages.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
