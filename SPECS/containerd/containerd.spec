# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           containerd
%define go_import_path  github.com/containerd/containerd/v2
%global commit          aad11006b869517fcd3009450b6f82da282e1a9b

Name:           containerd
Version:        2.3.3
Release:        %autorelease
Summary:        Industry-standard container runtime
License:        Apache-2.0
URL:            https://containerd.io
VCS:            git:https://github.com/containerd/containerd.git
#!RemoteAsset:  sha256:fcff2096ef20f1bc1d939bc55a8b831ea3eface574463fd7dc770b33ffe317b2
Source0:        https://github.com/containerd/containerd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:8ae9b2ee0114498438353ac489e98db2a03fb3ae44725d70ee318c7fbe7f2a64
Source1:        https://github.com/software-vendor/go-containerd-vendor/releases/download/v%{version}/containerd-v%{version}-vendor.tar.gz

BuildRequires:  go >= 1.26.3
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       runc
%{?systemd_requires}

%description
containerd is an industry-standard container runtime with an emphasis on
simplicity, robustness, and portability. It manages the complete container
lifecycle of its host system, including image transfer and storage, container
execution and supervision, low-level storage, and network attachments.
The CRI plugin is included for Kubernetes integration.

%prep
%autosetup -n %{name}-%{version}
rm -rf vendor
tar -xzf %{SOURCE1}

%build
export GO111MODULE=on
export GOFLAGS="-mod=vendor -trimpath -modcacherw"
export GOCACHE=%{_builddir}/go-build-cache
export CGO_ENABLED=0
%make_build VERSION=v%{version} REVISION=%{commit} \
    STATIC=1 GO_BUILD_FLAGS="-trimpath" \
    COMMANDS="ctr containerd containerd-shim-runc-v2" binaries

%install
install -Dpm0755 bin/containerd %{buildroot}%{_bindir}/containerd
install -Dpm0755 bin/containerd-shim-runc-v2 \
    %{buildroot}%{_bindir}/containerd-shim-runc-v2
install -Dpm0755 bin/ctr %{buildroot}%{_bindir}/ctr

install -Dpm0644 containerd.service %{buildroot}%{_unitdir}/containerd.service
sed -i 's#/usr/local/bin/containerd#%{_bindir}/containerd#' \
    %{buildroot}%{_unitdir}/containerd.service

install -d %{buildroot}%{_sysconfdir}/containerd
bin/containerd config default > %{buildroot}%{_sysconfdir}/containerd/config.toml

%check
%{buildroot}%{_bindir}/containerd --version
%{buildroot}%{_bindir}/ctr --version
%{buildroot}%{_bindir}/containerd-shim-runc-v2 --help >/dev/null
grep -q 'io.containerd.grpc.v1.cri' \
    %{buildroot}%{_sysconfdir}/containerd/config.toml

%post
%systemd_post containerd.service

%preun
%systemd_preun containerd.service

%postun
%systemd_postun_with_restart containerd.service

%files
%license LICENSE NOTICE vendor/modules.txt
%doc README.md RELEASES.md docs/
%{_bindir}/containerd
%{_bindir}/containerd-shim-runc-v2
%{_bindir}/ctr
%dir %{_sysconfdir}/containerd
%config(noreplace) %{_sysconfdir}/containerd/config.toml
%{_unitdir}/containerd.service

%changelog
%autochangelog
