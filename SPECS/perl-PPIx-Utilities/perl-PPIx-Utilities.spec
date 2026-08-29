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
#!RemoteAsset:  sha256:03a483386fd6a2c808f09778d44db06b02c3140fb24ba4bf12f851f46d3bcb9b
Source0:        https://www.cpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(Safe::Isa)
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

%files -f %{name}.files
%doc Changes README xt

%changelog
%autochangelog
