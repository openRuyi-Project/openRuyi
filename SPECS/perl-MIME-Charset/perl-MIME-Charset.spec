# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MIME-Charset
Version:        1.013.1
Release:        %autorelease
Summary:        Charset Information for MIME
License:        GPL-2.0-only
URL:            https://metacpan.org/dist/MIME-Charset
#!RemoteAsset:  sha256:1bb7a6e0c0d251f23d6e60bf84c9adefc5b74eec58475bfee4d39107e60870f0
Source0:        https://www.cpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
MIME::Charset provides information about character sets used for MIME
messages on Internet.

%files -f %{name}.files
%doc ARTISTIC Changes README

%changelog
%autochangelog
