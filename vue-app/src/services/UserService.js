function getQueryStringParams(searchTerm, offset) {
    let params= []
    if(searchTerm) params.push(`s=${encodeURIComponent(searchTerm)}`)
    if(searchTerm) params.push(`offset=${offset}`)

    if(params.length){
        return `?${params.join('&')}`
    } else {
        return '';
    }

}
export async function findStore(searchTerm, offset) {
    let queryParams = getQueryStringParams(searchTerm, offset);
    const response = await fetch(`/api/stores${queryParams}`);
    return await response.json()
}