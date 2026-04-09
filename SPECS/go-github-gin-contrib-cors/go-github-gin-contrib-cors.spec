# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cors
%define go_import_path  github.com/gin-contrib/cors

Name:           go-github-gin-contrib-cors
Version:        1.7.6
Release:        %autorelease
Summary:        Official CORS gin's middleware
License:        MIT
URL:            https://github.com/gin-contrib/cors
#!RemoteAsset
Source0:        https://github.com/gin-contrib/cors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/gin-contrib/cors) = %{version}

Requires:       go(github.com/gin-gonic/gin)
Requires:       go(github.com/stretchr/testify)

%description
CORS (Cross-Origin Resource Sharing) middleware for Gin
(https://github.com/gin-gonic/gin).

 * Enables flexible CORS handling for your Gin-based APIs.
 * Highly configurable: origins, methods, headers, credentials, and more.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
