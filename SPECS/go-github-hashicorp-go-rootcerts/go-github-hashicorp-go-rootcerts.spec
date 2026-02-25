# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-rootcerts
%define go_import_path  github.com/hashicorp/go-rootcerts

Name:           go-github-hashicorp-go-rootcerts
Version:        1.0.2
Release:        %autorelease
Summary:        Functions for loading root certificates for TLS connections.
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-rootcerts
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-rootcerts/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-rootcerts) = %{version}

%description
Functions for loading root certificates for TLS connections.

------------------------------------------------------------------------

Go's standard library crypto/tls provides a common mechanism for
configuring TLS connections in tls.Config. The RootCAs field on this
struct is a pool of certificates for the client to use as a trust store
when verifying server certificates.

This library contains utility functions for loading certificates
destined for that field, as well as one other important thing:

When the RootCAs field is nil, the standard library attempts to load the
host's root CA set.  This behavior is OS-specific, and the Darwin
implementation contains a bug that prevents trusted certificates from
the System and Login keychains from being loaded
(https://github.com/golang/go/issues/14514). This library contains
Darwin-specific behavior that works around that bug.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
