# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _test_target test-unit-local

Name:           skopeo
Version:        1.23.0
Release:        %autorelease
Summary:        Work with remote images registries - retrieving information, images, signing content
License:        Apache-2.0
URL:            https://github.com/podman-container-tools/skopeo
#!RemoteAsset:  sha256:de96bfc2bb523c852af675ffdadd934484812ce190aa8620e1d5fd6c51442e25
Source0:        https://github.com/podman-container-tools/skopeo/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  go
BuildRequires:  automake
BuildRequires:  go-md2man
BuildRequires:  pkgconfig(libbtrfsutil)
BuildRequires:  pkgconfig(gpgme)
# Required by signing-related unit tests.
BuildRequires:  gnupg

Requires:       containers-common

%description
skopeo is a command line utility that performs
various operations on container images and image repositories.

%conf
# No configuration needed

%install -a
# Remove common container configuration files provided by containers-common.
rm -rf %{buildroot}%{_sysconfdir}/containers
rm -rf %{buildroot}%{_sharedstatedir}/containers/sigstore

%files
%doc README.md
%license LICENSE
%{_bindir}/skopeo
%{_mandir}/man1/skopeo*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/skopeo
%dir %{fish_completions_dir}
%{fish_completions_dir}/skopeo.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_skopeo

%changelog
%autochangelog
