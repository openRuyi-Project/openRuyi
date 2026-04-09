# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
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
#!RemoteAsset
Source0:        https://github.com/golang/crypto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/golang/net/archive/v%{go_golang_x_net_version}.tar.gz#/net-%{go_golang_x_net_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-go.crypto/1%3A0.45.0-1/debian/patches/0001-skip-wycheproof_test.patch
Patch0:         2000-skip-wycheproof_test.patch

# https://go-review.googlesource.com/c/crypto/+/738760
Patch1:         0001-crypto-internal-poly1305-provide-optimised-assembly-for-riscv64.patch

BuildOption(prep):  -n %{_name}-%{version}
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
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
