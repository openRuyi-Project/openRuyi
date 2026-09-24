# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           containerd
%define go_import_path  github.com/containerd/containerd/v2
%global commit          1294c24a7da8e5a793ed378161673abe94118892

Name:           containerd
Version:        2.3.5
Release:        %autorelease
Summary:        Industry-standard container runtime
License:        Apache-2.0
URL:            https://containerd.io
VCS:            git:https://github.com/containerd/containerd.git
#!RemoteAsset:  sha256:a99a4dca98061064ff4cb35d27d1ec2345717e9108c822329fcec91dc72bff96
Source0:        https://github.com/containerd/containerd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
