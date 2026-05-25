# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           crypto
%define go_import_path  golang.org/x/crypto

# We need to to avoid circular dependency between go-golang-x-crypto and go-golang-x-net
# So we need to manually download the right version of golang.org/x/net and place it in the source tree
# Check https://github.com/golang/crypto/blob/master/go.mod for the correct version
%define go_golang_x_net_version 0.47.0

Name:           go-golang-x-crypto
Version:        0.46.0
Release:        %autorelease
Summary:        Go supplementary cryptography libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/crypto
VCS:            git:https://github.com/golang/crypto
#!RemoteAsset:  sha256:9dfbc96ebeb56e1bf71cd742c2a49494df9e68c4acf141bb6312e32b6c9e9ad1
Source0:        https://github.com/golang/crypto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:07079831acda4142a9eca62e3e989c2d86f956bac5365acf6a2dd3a8cfd73c26
Source1:        https://github.com/golang/net/archive/v%{go_golang_x_net_version}.tar.gz#/net-%{go_golang_x_net_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://go-review.googlesource.com/c/crypto/+/738760
Patch1:         0001-crypto-internal-poly1305-provide-optimised-assembly-for-riscv64.patch

# https://sources.debian.org/src/golang-go.crypto/1%3A0.45.0-1/debian/patches/0001-skip-wycheproof_test.patch
Patch2000:      2000-skip-wycheproof_test.patch

# TestWithPebble starts an external Pebble ACME server integration environment,
# which is not available in OBS.
# - HNO3Miracle
Patch2001:      2001-skip-pebble-integration-test.patch

BuildOption(check):  -skip TestWithPebble

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/crypto) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
This package provides cryptographic algorithms and protocols.

%prep -a
# Provide only the x/net idna subtree needed for tests without pulling the full go-golang-x-net package
mkdir -p vendor/golang.org/x/net
tar -xf %{SOURCE1} \
    --strip-components=1 \
    -C vendor/golang.org/x/net \
    net-%{go_golang_x_net_version}/idna
cat > vendor/modules.txt <<'EOF'
# golang.org/x/net v%{go_golang_x_net_version}
## explicit
golang.org/x/net/idna
EOF

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
