# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ceph-csi
Version:        3.17.0
Release:        %autorelease
Summary:        Container Storage Interface driver for Ceph
License:        Apache-2.0
URL:            https://github.com/ceph/ceph-csi
#!RemoteAsset:  sha256:bc5655bc0511bba6e990daa58a59aba3fd656989f9968e35d2199f4a7b4ac50b
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  ceph-devel
BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros

Requires:       ceph-common

Recommends:     kubernetes

%description
Ceph-CSI provides Container Storage Interface drivers for Ceph RBD, CephFS,
NFS, and NVMe-oF backends. This package installs the cephcsi binary and the
upstream Kubernetes deployment manifests.

%prep
%autosetup -n %{name}-%{version}

%build
export CGO_ENABLED=1
export GO111MODULE=on
export GOFLAGS="-mod=vendor -trimpath -modcacherw"
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/go-build-cache

%__go build %{go_build_flags_default} \
    -tags=tentacle,ceph_preview \
    -ldflags "-X github.com/ceph/ceph-csi/internal/util.GitCommit=openruyi -X github.com/ceph/ceph-csi/internal/util.DriverVersion=v%{version}" \
    -o cephcsi ./cmd/

%install
install -Dpm0755 cephcsi %{buildroot}%{_bindir}/cephcsi

install -dpm0755 %{buildroot}%{_datadir}/kubernetes/%{name}
cp -a deploy %{buildroot}%{_datadir}/kubernetes/%{name}/
cp -a examples/rbd %{buildroot}%{_datadir}/kubernetes/%{name}/examples-rbd

%check
%{buildroot}%{_bindir}/cephcsi --version
%{buildroot}%{_bindir}/cephcsi --help >/dev/null

%files
%doc README.md PendingReleaseNotes.md vendor/modules.txt
%license LICENSE
%{_bindir}/cephcsi
%{_datadir}/kubernetes/%{name}

%changelog
%autochangelog
