# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ocicrypt
%define go_import_path  github.com/containers/ocicrypt

Name:           go-github-containers-ocicrypt
Version:        1.3.2
Release:        %autorelease
Summary:        OCI image encryption library for Go
License:        Apache-2.0
URL:            https://github.com/containers/ocicrypt
#!RemoteAsset:  sha256:8f7ca19c2881c674dc09e5ba79fbba2d13adb4ef160977fd384f19b70f000912
Source0:        https://github.com/containers/ocicrypt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  gnutls
BuildRequires:  softhsm
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/miekg/pkcs11)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/smallstep/pkcs7)
BuildRequires:  go(github.com/stefanberger/go-pkcs11uri)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/containers/ocicrypt) = %{version}

Requires:       go
Requires:       go-rpm-macros
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/miekg/pkcs11)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/smallstep/pkcs7)
Requires:       go(github.com/stefanberger/go-pkcs11uri)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/term)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/protobuf)

%description
ocicrypt provides encryption and decryption support for OCI images.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
