# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-CPAN-Meta
Version:        2.150010
Release:        %autorelease
Summary:        Distribution metadata for a CPAN dist
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CPAN-Meta
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.011
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.20
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(version) >= 0.88

%description
Software distributions released to the CPAN include a META.json or, for
older distributions, META.yml, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is described
in CPAN::Meta::Spec.

%prep
%setup -q -n CPAN-Meta-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README Todo

%changelog
%autochangelog
