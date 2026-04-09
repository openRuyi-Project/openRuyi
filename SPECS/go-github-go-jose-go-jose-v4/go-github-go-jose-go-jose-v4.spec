# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jose
%define go_import_path  github.com/go-jose/go-jose

Name:           go-github-go-jose-go-jose-v4
Version:        4.1.3
Release:        %autorelease
Summary:        An implementation of JOSE standards (JWE, JWS, JWT) in Go
License:        Apache-2.0
URL:            https://github.com/go-jose/go-jose
#!RemoteAsset
Source0:        https://github.com/go-jose/go-jose/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-jose/go-jose/v4) = %{version}

%description
Package jose aims to provide an implementation of the Javascript Object
Signing and Encryption set of standards. This includes support for JSON
Web Encryption, JSON Web Signature, and JSON Web Token standards.

Overview

The implementation follows the JSON Web Encryption
(https://dx.doi.org/10.17487/RFC7516) (RFC 7516), JSON Web Signature
(https://dx.doi.org/10.17487/RFC7515) (RFC 7515), and JSON Web Token
(https://dx.doi.org/10.17487/RFC7519) (RFC 7519) specifications. Tables
of supported algorithms are shown below. The library supports both the
compact and JWS/JWE JSON Serialization formats, and has optional support
for multiple recipients. It also comes with a small command-line utility
(jose-util (https://pkg.go.dev/github.com/go-jose/go-jose/jose-util))
for dealing with JOSE messages in a shell.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
