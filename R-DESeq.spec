%define		packname	DESeq

Summary:	Differential gene expression analysis based on the negative binomial distribution
Name:		R-%{packname}
Version:	1.14.0
Release:	2
License:	GPL v3
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	6df447df70a5c2e1fac6c98540f6b249
URL:		http://bioconductor.org/packages/release/bioc/html/DESeq.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-cran-locfit
BuildRequires:	R-genefilter
BuildRequires:	R-geneplotter
BuildRequires:	R-cran-RColorBrewer
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-Biobase
Requires:	R-cran-locfit
Requires:	R-genefilter
Requires:	R-geneplotter
Requires:	R-cran-RColorBrewer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Estimate variance-mean dependence in count data from high-throughput
sequencing assays and test for differential expression based on a
model using the negative binomial distribution.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/extra
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/CITATION
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
