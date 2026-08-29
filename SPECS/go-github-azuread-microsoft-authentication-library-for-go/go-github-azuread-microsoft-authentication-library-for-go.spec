# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           microsoft-authentication-library-for-go
%define go_import_path  github.com/AzureAD/microsoft-authentication-library-for-go

# MSAL is a runtime dependency of the Azure SDK's azidentity. Some unit tests
# spin up local HTTP servers; run them but tolerate environment-related
# failures. Use the define form, which golangmodules honours.
%define go_test_ignore_failure 1

Name:           go-github-azuread-microsoft-authentication-library-for-go
Version:        1.6.0
Release:        %autorelease
Summary:        Microsoft Authentication Library (MSAL) for Go
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-go
#!RemoteAsset:  sha256:af01868d48df6d4419afb01a3b2db747d255323e38ad6e7a81e3427dd9fe583a
Source0:        https://github.com/AzureAD/microsoft-authentication-library-for-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/pkg/browser)

Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go) = %{version}
Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go/apps/cache) = %{version}
Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go/apps/confidential) = %{version}
Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go/apps/errors) = %{version}
Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go/apps/managedidentity) = %{version}
Provides:       go(github.com/AzureAD/microsoft-authentication-library-for-go/apps/public) = %{version}

Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/kylelemons/godebug)
Requires:       go(github.com/pkg/browser)

# apps/tests holds standalone test programs (integration/performance/devapps)
# that need network access, real credentials and extra deps (e.g.
# montanaflynn/stats) not required by the library; drop them so the build
# does not pull those in.
%prep -a
rm -rf apps/tests

%description
The Microsoft Authentication Library (MSAL) for Go enables applications to
authenticate users and acquire tokens from the Microsoft identity platform.
It is the runtime authentication backend used by the Azure SDK's azidentity
module, which Prometheus' Azure service discovery depends on.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
