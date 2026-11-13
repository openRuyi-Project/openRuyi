# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gce-tcb-verifier
%define go_import_path  github.com/google/gce-tcb-verifier

Name:           go-github-google-gce-tcb-verifier
Version:        0.3.1
Release:        %autorelease
Summary:        Go libraries for verifying Google Compute Engine TCB attestations
License:        Apache-2.0
URL:            https://github.com/google/gce-tcb-verifier
#!RemoteAsset:  sha256:c6c4421a6b6e61e64d444d05ec3251dbc24204530ff76b7d1eee0eb1f6b46d01
Source0:        https://github.com/google/gce-tcb-verifier/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/kms)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-configfs-tsm)
BuildRequires:  go(github.com/google/go-sev-guest)
BuildRequires:  go(github.com/google/go-tdx-guest)
BuildRequires:  go(github.com/google/go-tpm-tools)
BuildRequires:  go(github.com/google/logger)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/gce-tcb-verifier) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/cmd) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/cmd/output) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/endorse) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/eventlog) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/extract) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/extract/eventlog) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/extract/extractsev) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/extract/extracttdx) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement/cmd) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement/parsepath) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement/parsepath/testmessage) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement/testing) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/keys) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/keys/gcpkms) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/ovmf) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/ovmf/abi) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/certificates) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/endorsement) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/events) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/ovmf) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/releases) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/scrtmversion) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/proto/sev) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/rotate) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sev) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/gcsca) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/memca) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/nonprod) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/ops) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/transform) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/sign/types) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/storage/local) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/storage/ops) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/storage/storagei) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/tdx) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/devkeys) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/fakeovmf) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/match) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod/certs) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod/localca) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod/localkm) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod/localnonvcs) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/nonprod/memkm) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/storage) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/testca) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/testkm) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/testkms) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/testing/testsign) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/timeproto) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/verify) = %{version}
Provides:       go(github.com/google/gce-tcb-verifier/verify/verifytest) = %{version}

Requires:       go(cloud.google.com/go/iam)
Requires:       go(cloud.google.com/go/kms)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-configfs-tsm)
Requires:       go(github.com/google/go-sev-guest)
Requires:       go(github.com/google/go-tdx-guest)
Requires:       go(github.com/google/go-tpm-tools)
Requires:       go(github.com/google/logger)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/inconshreveable/mousetrap)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package verifies Google Compute Engine trusted computing base attestations and includes the endorsement generation module.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
