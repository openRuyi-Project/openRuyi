# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           containers-common
Version:        0.67.0
Release:        %autorelease
Summary:        Common libraries and configuration for container tools
License:        Apache-2.0
URL:            https://github.com/containers/container-libs
#!RemoteAsset:  sha256:503756a080d66141fc3103952b6a5c0253c45da8475673c8d4ee5c948f4dade4
Source:         https://github.com/containers/container-libs/archive/refs/tags/common/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  go
BuildRequires:  go-md2man

%description
Monorepository with libraries used by the containers projects.

%prep
%autosetup -n container-libs-common-v%{version}

%build
mkdir -p man5
for i in common/docs/*.5.md image/docs/*.5.md storage/docs/*.5.md; do
   go-md2man -in $i -out man5/$(basename $i .md)
done

%install
install -dp %{buildroot}%{_sysconfdir}/containers/{certs.d,oci/hooks.d,networks,registries.conf.d,registries.d,systemd}
install -dp %{buildroot}%{_sharedstatedir}/containers/sigstore
install -dp %{buildroot}%{_datadir}/containers/systemd
install -dp %{buildroot}%{_prefix}/lib/containers/storage
install -dp -m 700 %{buildroot}%{_prefix}/lib/containers/storage/{overlay-images,overlay-layers}
touch %{buildroot}%{_prefix}/lib/containers/storage/overlay-images/images.lock
touch %{buildroot}%{_prefix}/lib/containers/storage/overlay-layers/layers.lock
install -Dp -m0644 image/default.yaml %{buildroot}%{_sysconfdir}/containers/registries.d/default.yaml
install -Dp -m0644 image/default-policy.json %{buildroot}%{_sysconfdir}/containers/policy.json
install -Dp -m0644 image/registries.conf %{buildroot}%{_sysconfdir}/containers/registries.conf
install -Dp -m0644 storage/storage.conf %{buildroot}%{_datadir}/containers/storage.conf
install -m0644 common/pkg/subscriptions/mounts.conf %{buildroot}%{_datadir}/containers/mounts.conf
install -m0644 common/pkg/seccomp/seccomp.json %{buildroot}%{_datadir}/containers/seccomp.json
install -m0644 common/pkg/config/containers.conf %{buildroot}%{_datadir}/containers/containers.conf
for i in man5/*.5; do
    install -Dp -m0644 $i -t %{buildroot}%{_mandir}/man5
done
ln -s containerignore.5 %{buildroot}%{_mandir}/man5/.containerignore.5

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/certs.d
%dir %{_sysconfdir}/containers/networks
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.conf.d
%dir %{_sysconfdir}/containers/registries.d
%dir %{_sysconfdir}/containers/systemd
%dir %{_prefix}/lib/containers
%dir %{_prefix}/lib/containers/storage
%dir %{_prefix}/lib/containers/storage/overlay-images
%dir %{_prefix}/lib/containers/storage/overlay-layers
%{_prefix}/lib/containers/storage/overlay-images/images.lock
%{_prefix}/lib/containers/storage/overlay-layers/layers.lock
%config(noreplace) %{_sysconfdir}/containers/policy.json
%config(noreplace) %{_sysconfdir}/containers/registries.conf
%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%ghost %{_sysconfdir}/containers/storage.conf
%ghost %{_sysconfdir}/containers/containers.conf
%dir %{_sharedstatedir}/containers/sigstore
%dir %{_datadir}/containers
%dir %{_datadir}/containers/systemd
%{_datadir}/containers/storage.conf
%{_datadir}/containers/containers.conf
%{_datadir}/containers/mounts.conf
%{_datadir}/containers/seccomp.json
%{_mandir}/man5/*.5*
%{_mandir}/man5/.containerignore.5*

%changelog
%autochangelog
