# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           postgresql-pgvector
Version:        0.8.7
Release:        %autorelease
Summary:        Vector similarity search for PostgreSQL
License:        PostgreSQL
URL:            https://github.com/pgvector/pgvector
VCS:            git:https://github.com/pgvector/pgvector.git
#!RemoteAsset:  sha256:cac0b10c360f05b2d521200105ba3697e773d4cd3731f5a915a7e37ebe0bea85
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  diffutils
BuildRequires:  postgresql(major) = 19
BuildRequires:  postgresql-server
BuildRequires:  postgresql-contrib
BuildRequires:  perl
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Test::More)
Requires:       postgresql-server(:MODULE_COMPAT_19)

%description
pgvector adds vector types, distance operators, and HNSW and IVFFlat indexes
to PostgreSQL. Enable it in a database with CREATE EXTENSION vector.

%package        devel
Summary:        Development headers for PostgreSQL vector extensions
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       postgresql(major) = 19

%description    devel
These headers let other PostgreSQL extensions use pgvector data types.

%prep
%autosetup -n pgvector-%{version}

%build
%set_build_flags
%make_build OPTFLAGS="" with_llvm=no CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

%install
%make_install OPTFLAGS="" with_llvm=no

%check
# Load the staged extension without changing the installed PostgreSQL files.
cat > test.conf <<'EOF'
extension_control_path = '%{buildroot}%{_datadir}/postgresql:$system'
dynamic_library_path = '%{buildroot}%{_libdir}/postgresql:$libdir'
EOF
%make_build OPTFLAGS="" with_llvm=no installcheck \
    REGRESS_OPTS="--inputdir=test --load-extension=vector --temp-instance=$PWD/tmp_regress --temp-config=$PWD/test.conf"
TEMP_CONFIG="$PWD/test.conf" %make_build OPTFLAGS="" with_llvm=no prove_installcheck

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/postgresql/vector.so
%{_datadir}/postgresql/extension/vector.control
%{_datadir}/postgresql/extension/vector--*.sql

%files devel
%license LICENSE
%{_includedir}/postgresql/server/extension/vector/

%changelog
%autochangelog
