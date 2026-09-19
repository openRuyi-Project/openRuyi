# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kes
%define go_import_path  github.com/minio/kes
%define commit_id       f5bed15f4d0a2190befae3adf38e84ac124c9468

Name:           kes
Version:        0.24.0+git20250130.f5bed15
Release:        %autorelease
Summary:        Key encryption server and client
License:        AGPL-3.0-only
URL:            https://github.com/minio/kes
#!RemoteAsset:  sha256:ee3923cb185ad54bfba303b3e7a0413f5d6c0666c0cec58346bd91757efd10c4
Source0:        https://github.com/minio/kes/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# Source includes https://github.com/minio/kes/pull/506 (KMS enclave API).
# Use the private-key parser required by the distribution KMS client.
Patch2000:      2000-adapt-migration-to-current-kms-api.patch
# Report the release and source commit when building without a .git directory.
Patch2001:      2001-allow-archive-build-version-metadata.patch
# Format the numeric Fortanix response status correctly; keep vet enabled.
Patch2002:      2002-format-fortanix-http-status.patch

BuildOption(check):  -timeout=15m

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/mem)
BuildRequires:  go(aead.dev/minisign)
BuildRequires:  go(aead.dev/mtls)
BuildRequires:  go(cloud.google.com/go/secretmanager)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/hashicorp/vault/api)
BuildRequires:  go(github.com/minio/kms-go/kes)
BuildRequires:  go(github.com/minio/kms-go/kms)
BuildRequires:  go(github.com/minio/selfupdate)
BuildRequires:  go(github.com/muesli/termenv)
# The current msgp source RPM does not yet require its fwd runtime dependency.
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

%description
KES provides a key encryption service and a command-line client, with
policy-based access and supported external key-store backends.

%package     -n go-github-minio-kes
Summary:        Reusable Go source for the KES server and client
BuildArch:      noarch
Provides:       go(github.com/minio/kes) = %{version}
Requires:       go(aead.dev/mem)
Requires:       go(aead.dev/minisign)
Requires:       go(aead.dev/mtls)
Requires:       go(cloud.google.com/go/secretmanager)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/hashicorp/vault/api)
Requires:       go(github.com/minio/kms-go/kes)
Requires:       go(github.com/minio/kms-go/kms)
Requires:       go(github.com/minio/selfupdate)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/philhofer/fwd)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description -n go-github-minio-kes
Reusable KES server, client and configuration packages, including the API
used by the MinIO Console.

%build
# KES keeps its executable entry point under cmd/kes.
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -ldflags "-X %{go_import_path}/internal/sys.Version=%{version} -X %{go_import_path}/internal/sys.CommitID=%{commit_id}" \
    -o %{_name} %{go_import_path}/cmd/%{_name}

%install -a
# Keep the installed Go source free of the executable.
rm -f %{_name}
%buildsystem_golangmodules_install

%check -a
cd %{_builddir}/go/src/%{go_import_path}
# The filesystem backend can be exercised without external credentials.
mkdir -p %{_builddir}/kes-test-keys
%__go test %{go_test_flags_default} -timeout 5m ./kesconf -run '^TestFS$' -args -fs.path=%{_builddir}/kes-test-keys
%{buildroot}%{_bindir}/%{_name} --version > kes-version.txt
cat kes-version.txt
grep -F "%{version}" kes-version.txt
grep -F "%{commit_id}" kes-version.txt

%files
%doc README.md server-config.yaml
%license LICENSE
%{_bindir}/kes

%files -n go-github-minio-kes
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
