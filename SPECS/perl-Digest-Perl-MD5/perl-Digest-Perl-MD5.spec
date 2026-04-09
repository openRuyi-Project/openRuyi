# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-Perl-MD5
Version:        1.9
Release:        %autorelease
Summary:        Digest::Perl::MD5 Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Digest-Perl-MD5
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DE/DELTA/Digest-Perl-MD5-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This modules has the same interface as the much faster Digest::MD5. So you
can easily exchange them, e.g.

%prep
%setup -q -n Digest-Perl-MD5-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES rand.f

%changelog
%autochangelog
