# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-JSON
Version:        4.10
Release:        %autorelease
Summary:        JSON (JavaScript Object Notation) encoder/decoder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/JSON-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS) >= 2.34
BuildRequires:  perl(Test::More)

Requires:       perl(JSON::XS) >= 2.34

%description
This module is a thin wrapper for JSON::XS-compatible modules with a few
additional features. All the backend modules convert a Perl data structure
to a JSON text and vice versa. This module uses JSON::XS by default, and
when JSON::XS is not available, falls back on JSON::PP, which is in the
Perl core since 5.14. If JSON::PP is not available either, this module
then falls back on JSON::backportPP (which is actually JSON::PP in a
different .pm file) bundled in the same distribution as this module. You
can also explicitly specify to use Cpanel::JSON::XS, a fork of JSON::XS by
Reini Urban.

%prep
%setup -q -n JSON-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
