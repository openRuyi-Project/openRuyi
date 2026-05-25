# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           enterprise-certificate-proxy
%define go_import_path  github.com/googleapis/enterprise-certificate-proxy
# Darwin and Windows packages import platform-specific subpackages excluded by
# Linux build tags. Linux pkcs11 tests require softhsm, and http_proxy contains
# routing assertions that fail under the OBS test environment. - HNO3Miracle
%define go_test_exclude %{shrink:
    github.com/googleapis/enterprise-certificate-proxy/darwin
    github.com/googleapis/enterprise-certificate-proxy/http_proxy
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/darwin
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/linux/pkcs11
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/windows
    github.com/googleapis/enterprise-certificate-proxy/linux
    github.com/googleapis/enterprise-certificate-proxy/windows
}

Name:           go-github-googleapis-enterprise-certificate-proxy
Version:        0.3.16
Release:        %autorelease
Summary:        Enterprise certificate proxy library for Go
License:        Apache-2.0
URL:            https://github.com/googleapis/enterprise-certificate-proxy
#!RemoteAsset:  sha256:0d40c4c4f2ae8b638061e04754f333a4b6ca411e16dc6ca63ae92fa4534b1eb7
Source0:        https://github.com/googleapis/enterprise-certificate-proxy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-pkcs11)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/googleapis/enterprise-certificate-proxy) = %{version}

Requires:       go(github.com/google/go-pkcs11)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
This package provides Go helpers for enterprise certificate based authentication.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
