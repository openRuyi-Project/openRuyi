# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           podman
Version:        5.8.2
Release:        %autorelease
Summary:        Manage containers, images, pods, and their volumes
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://podman.io/
VCS:            git:https://github.com/containers/podman
#!RemoteAsset:  sha256:b20ea65afc5a58ea1cea019bd51a5d84eb9042d25d3eb82c55010c8815732d84
Source0:        https://github.com/containers/podman/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  BUILDFLAGS=-trimpath
BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  BINDIR=%{_bindir}
BuildOption(build):  TMPFILESDIR=%{_tmpfilesdir}
BuildOption(build):  MANDIR=%{_mandir}
BuildOption(build):  ETCDIR=%{_sysconfdir}
BuildOption(build):  LIBEXECDIR=%{_libexecdir}
BuildOption(install):  install.completions
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  TMPFILESDIR=%{_tmpfilesdir}
BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  ETCDIR=%{_sysconfdir}
BuildOption(install):  LIBEXECDIR=%{_libexecdir}

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  groff
BuildRequires:  make
BuildRequires:  man
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libbtrfsutil)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python
BuildRequires:  systemd-rpm-macros

Requires:       containers-common
Requires:       conmon
Requires:       crun
Requires:       passt
Requires:       netavark

%description
Podman (the POD MANager) is a tool for managing containers and images,
volumes mounted into those containers, and pods made from groups of
containers.

# no configure scripts
%conf

# TODO: enable tests when we have bats
%check

%files
%doc README.md CONTRIBUTING.md install.md transfer.md
%license LICENSE vendor/modules.txt
%{_bindir}/podman
%{_bindir}/podman-remote
%{_bindir}/podmansh
%{_datadir}/bash-completion/completions/podman*
%{_datadir}/fish/vendor_completions.d/podman*.fish
%{_datadir}/zsh/site-functions/_podman*
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/quadlet
%{_libexecdir}/podman/rootlessport
%{_mandir}/man*/podman*
%{_mandir}/man5/quadlet.5.*
%{_systemdgeneratordir}/podman-system-generator
%{_systemdusergeneratordir}/podman-user-generator
%{_tmpfilesdir}/podman.conf
%{_unitdir}/podman*
%{_userunitdir}/podman*

%changelog
%autochangelog
