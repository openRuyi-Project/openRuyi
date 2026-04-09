# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PPIx-Utilities
Version:        1.001000
Release:        %autorelease
Summary:        Extensions to PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PPIx-Utilities
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PPI) >= 1.208
BuildRequires:  perl(PPI::Document) >= 1.208
BuildRequires:  perl(PPI::Document::Fragment) >= 1.208
BuildRequires:  perl(PPI::Dumper) >= 1.208
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Readonly::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(PPI) >= 1.208
Requires:       perl(PPI::Document::Fragment) >= 1.208

%description
This is a collection of functions for dealing with PPI objects, many of
which originated in Perl::Critic. They are organized into modules by the
kind of PPI class they relate to, by replacing the "PPI" at the front of
the module name with "PPIx::Utilities", e.g. functionality related to
PPI::Nodes is in PPIx::Utilities::Node.

%prep
%setup -q -n PPIx-Utilities-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README xt

%changelog
%autochangelog
