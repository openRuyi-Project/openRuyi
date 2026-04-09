# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypiname mupdf

Name:           mupdf
Version:        1.27.2
Release:        %autorelease
Summary:        A lightweight PDF viewer and toolkit
License:        AGPL-3.0-or-later
URL:            https://mupdf.com/
VCS:            git:https://github.com/ArtifexSoftware/mupdf
#!RemoteAsset:  sha256:553867b135303dc4c25ab67c5f234d8e900a0e36e66e8484d99adc05fe1e8737
Source0:        https://mupdf.com/downloads/archive/mupdf-%{version}-source.tar.gz
Source1:        mupdf.desktop
Source2:        mupdf-gl.desktop
BuildSystem:    autotools

BuildOption(build):  shared c++
BuildOption(build):  XCFLAGS="%{build_cflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
BuildOption(build):  XCXXFLAGS="%{build_cxxflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  libdir=%{_libdir}
BuildOption(install):  pydir=%{python3_sitearch}
BuildOption(install):  SO_INSTALL_MODE=755
BuildOption(install):  install install-shared-c install-shared-c++

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  binutils
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(jbig2dec)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(libclang)
BuildRequires:  python3dist(swig)
BuildRequires:  pyproject-rpm-macros

%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.

%package        devel
Summary:        C Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for mupdf library.

%package     -n python-%{pypiname}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{pypiname}
%python_provide python3-%{pypiname}

%description -n python-%{pypiname}
The python3-%{pypiname} package contains low level mupdf python bindings.

%prep -a
for d in $(ls thirdparty | grep -v -e extract -e lcms2 -e mujs); do
	rm -rf thirdparty/$d
done
rm -f docs/README

echo > user.make "\
	LD := ld.bfd
	USE_SYSTEM_LIBS := yes
	USE_SYSTEM_MUJS := no # build needs source anyways
	USE_TESSERACT := no
	VENV_FLAG :=
	barcode := no
	build := release
	shared := yes
	verbose := yes
"

sed -i -e '/^install-shared-c++:/s/ c++//' Makefile
sed -i -e '/^install-shared-python:/s/ python//' Makefile
sed -i -e '/DZXING_EXPERIMENTAL_API/ d' Makelists
sed -i -e 's/barcode=yes/barcode=no/' scripts/wrap/__main__.py

# No configure.
%conf

%generate_buildrequires
%pyproject_buildrequires -R

%build -a
export MUPDF_SETUP_BUILD_DIR=build/shared-release
export MUPDF_SETUP_VERSION=%{version}
%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files -L %{pypiname}

rm -rf %{buildroot}/%{_docdir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf.svg
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf-gl.svg

cd %{buildroot}/%{_bindir} && ln -s %{name}-x11 %{name}

%check
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %{py3_test_envvars} %{python3} scripts/mupdfwrap_test.py thirdparty/lcms2/doc/*.pdf

%files
%license COPYING
%doc README CHANGES docs/*
%{_bindir}/*
%{_datadir}/applications/mupdf*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*.1*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/mupdf
%{_libdir}/lib*.so

%files -n python-%{pypiname} -f %{pyproject_files}
%license COPYING
%{python3_sitearch}/_mupdf.so
%{python3_sitearch}/libmupdf.so.27*
%{python3_sitearch}/libmupdfcpp.so.27*

%changelog
%autochangelog
