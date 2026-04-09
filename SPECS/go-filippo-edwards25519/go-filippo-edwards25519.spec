# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           edwards25519
%define go_import_path  filippo.io/edwards25519

Name:           go-filippo-edwards25519
Version:        1.1.0
Release:        %autorelease
Summary:        filippo.io/edwards25519 — A safer, faster, and more powerful low-level edwards25519 Go implementation.
License:        BSD-3-Clause
URL:            https://github.com/FiloSottile/edwards25519
#!RemoteAsset
Source0:        https://github.com/FiloSottile/edwards25519/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(filippo.io/edwards25519) = %{version}

%description
This library implements the edwards25519 elliptic curve, exposing the
necessary APIs to build a wide array of higher-level primitives. Read
the docs at pkg.go.dev/filippo.io/edwards25519

The package tracks the upstream standard library package
crypto/internal/fips140/edwards25519 and extends it with additional
functionality.

The code is originally derived from Adam Langley's internal
implementation in the Go standard library, and includes George
Tankersley's performance improvements (https://golang.org/cl/71950). It
was then further developed by Henry de Valence for use in ristretto255,
and was finally merged back into the Go standard library
(https://golang.org/cl/276272) as of Go 1.17.

Most users don't need this package, and should instead use
crypto/ed25519 for signatures, crypto/ecdh for Diffie-Hellman, or
github.com/gtank/ristretto255 for prime order group logic. However, for
anyone currently using a fork of the internal edwards25519 package or of
github.com/agl/edwards25519, this package should be a safer, faster, and
more powerful alternative.

Since this package is meant to curb proliferation of edwards25519
implementations in the Go ecosystem, it welcomes requests for new APIs
or reviewable performance improvements.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
