# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mongo-driver
%define go_import_path  go.mongodb.org/mongo-driver/v2
# These tests require MongoDB, a container runtime, or external network access.
%define go_test_exclude %{shrink:
    %{go_import_path}/internal/cmd/benchmark
    %{go_import_path}/internal/docexamples
    %{go_import_path}/internal/integration
    %{go_import_path}/internal/integration/unified
    %{go_import_path}/internal/test/compilecheck
    %{go_import_path}/internal/test/goleak
    %{go_import_path}/mongo
    %{go_import_path}/mongo/options
    %{go_import_path}/x/mongo/driver/connstring
    %{go_import_path}/x/mongo/driver/integration
    %{go_import_path}/x/mongo/driver/topology
}
%define specifications_commit ea6be202feb255242077cbc53527559e79e5cd00

Name:           go-mongodb-mongo-driver-v2
Version:        2.8.0
Release:        %autorelease
Summary:        MongoDB driver for Go
License:        Apache-2.0
URL:            https://github.com/mongodb/mongo-go-driver
#!RemoteAsset:  sha256:9c8297e35821dd8277c968ceefcb4971bcb8e875d4bed4417d127ee5a968bcbb
Source0:        https://github.com/mongodb/mongo-go-driver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Restore the specifications submodule revision pinned by upstream.
#!RemoteAsset:  sha256:4011f4ebf0e25b6d477be87a1cb03b86dad13d0adb5f7e558ae53e5a13877900
Source1:        https://github.com/mongodb/specifications/archive/%{specifications_commit}.tar.gz#/%{_name}-specifications-%{specifications_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport the test format fixes from upstream.
# https://github.com/mongodb/mongo-go-driver/commit/d20c5dbbd8288f43ed462c8aa74edac2d76a3cb7
Patch1000:      1000-Fix-non-constant-test-format-strings.patch

BuildOption(prep):  -N

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/aws/aws-lambda-go)
BuildRequires:  go(github.com/bitfield/script)
BuildRequires:  go(github.com/bombsimon/logrusr/v4)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/zapr)
BuildRequires:  go(github.com/go-logr/zerologr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/testcontainers/testcontainers-go)
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/bitfield/script)
Requires:       go(github.com/bombsimon/logrusr/v4)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-logr/zapr)
Requires:       go(github.com/go-logr/zerologr)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/rs/zerolog)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/xdg-go/scram)
Requires:       go(github.com/xdg-go/stringprep)
Requires:       go(github.com/youmark/pkcs8)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sync)

%description
The official MongoDB Go driver provides BSON handling, connection pooling,
authentication, sessions, transactions, change streams, and client APIs.

%prep -a
%patch -P 1000 -p1
rm -rf testdata/specifications
mkdir -p testdata/specifications
tar -xf %{SOURCE1} --strip-components=1 -C testdata/specifications

%check
export TZ=America/New_York
%buildsystem_golangmodules_check
for pkg in %{go_test_exclude}; do
    go test -c -o /dev/null "$pkg"
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
