# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           buildah
Version:        1.43.1
Release:        %autorelease
Summary:        A tool that facilitates building OCI images
License:        Apache-2.0
URL:            https://github.com/containers/buildah
#!RemoteAsset:  sha256:7980a8b4fb719a104d592b06de149cc18766de02f8c3dd94e727f8702a62f9cd
Source:         https://github.com/containers/buildah/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  go
BuildRequires:  make
BuildRequires:  fdupes
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libassuan)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  btrfs-progs-devel

Requires:       netavark
Requires:       containers-common
Requires:       runc >= 1.0.2

%description
A tool that facilitates building OCI images.

# No configure.
%conf

%install -a
install -D -m 0644 contrib/completions/bash/buildah %{buildroot}%{bash_completions_dir}/buildah

# No tests.
%check

%files
%license LICENSE
%{_mandir}/man1/buildah*
%{_bindir}/buildah
%{_datadir}/bash-completion/completions/buildah

%changelog
%autochangelog
