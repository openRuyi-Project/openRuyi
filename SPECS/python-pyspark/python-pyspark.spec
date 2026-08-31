# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyspark

Name:           python-%{srcname}
Version:        4.2.0
Release:        %autorelease
Summary:        Apache Spark Python API
License:        Apache-2.0
URL:            https://spark.apache.org/
VCS:            git:https://github.com/apache/spark.git
#!RemoteAsset:  sha256:5ad689d53570ee1674193fd4f9bda065f0db3be9363a27d2a3406cc457b70b61
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pyspark
# PySparkRuntimeError: [JAVA_GATEWAY_EXITED] Java gateway process exited before sending its port number.
BuildOption(check):  -e 'pyspark.python.pyspark.shell'
BuildOption(check):  -e 'pyspark.shell'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(grpcio-status)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(py4j)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(zstandard)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings and command-line tools for Apache Spark.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE NOTICE
%exclude %{_bindir}/*.cmd
%exclude %{python3_sitelib}/pyspark/bin/*.cmd
%{_bindir}/beeline
%{_bindir}/docker-image-tool.sh
%{_bindir}/find-spark-home
%{_bindir}/find_spark_home.py
%{_bindir}/load-spark-env.sh
%{_bindir}/pyspark
%{_bindir}/run-example
%{_bindir}/spark-class
%{_bindir}/spark-connect-shell
%{_bindir}/spark-pipelines
%{_bindir}/spark-shell
%{_bindir}/spark-sql
%{_bindir}/spark-submit
%{_bindir}/sparkR

%changelog
%autochangelog
